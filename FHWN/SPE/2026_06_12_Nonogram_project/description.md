# Database schema

Informal description of [`DDL.sql`](DDL.sql). 

Assumption/convention: 
 - if any puzzle of size nxm is there, then all the puzzles with lower dimensions are.
 - "mostly addition only" tables 
 - The DDL dump does not enforce some constraints described below

### `Pictures` table
   - `id` - autoincrement
   - `height`
   - `width`
   - `pixels` - binary
   - `smallest_equivalent_id`

(`height`, `width`, `pixels`) is unique (candidate key)

Nothing can be `null`, everything is "const", and nothing will be deleted.

`pixels` is just a top-to-bottom concatenation of rows with 1 for black/filled/`██` pixels, and 0 for white/empty/`░░` ones.

For example `010001111` for this:
```
░░██░░
░░░░██
██████
```
> [!NOTE]
> `pixels` alone is not a unique identifier
> `00110101` can describe all of these:
>
> ```
> ░░░░████░░██░░██
> ```
>
> ```
> ░░░░████
> ░░██░░██
> ```
>
> ```
> ░░░░
> ████
> ░░██
> ░░██
> ```
>
> ```
> ░░
> ░░
> ██
> ██
> ░░
> ██
> ░░
> ██
> ```
> (`height`, `pixels`) would be enough though, but we accept this redundancy.


### `Puzzles` table
 - `picture_id` - PK and FK on `Pictures/id`
 - `clues` - JSON
 - `locally_solvable` - bool

Only additions, no deletion.

Initially `locally_solvable` is set to `null`. Later only this is updated with a boolean value, and only once.

The JSON format for the clues is like this, but all the whitespaces removed, most condensed version.

```json
{
  "row_clues" : [
    [1,1,2],
    [2,1]
    ...
  ],
  "column_clues" : [
    [1,1,2],
    [2,1]
    ...
  ],
}
```

### `Solutions` table
 - `id` - autoincrement
 - `picture_id` - as above
 - `solution_time` (in seconds)
 - `solver_name` (string)
 - `solver_version` int
 - `configuration` - JSON

Only additions.

The last will be used for logging environment / configuration (e.g. cache size) info.

`solver_name` shouldbe Bun / Node / Java / c#. Versions are freely incremented.


# Minimal picture logic

Two pictures are equivalent if we can get from one to another by:
 - rotation
 - mirroring
 - adding/removing empty lines/rows from the sides
 - adding removing additional empty rows/columns next to a "middle" empty row/column

The ordering among them is the lexicographic ordering of (`height`, `width`, `pixels`).

Finding the minimal one:
 1. remove all the unnecessary empty lines
 2. if not a square, take the landscape rotations, otherwise all 4.
 3. take the mirrorings
 4. calculate the `pixels`, select the one with the smallest.

## Example

Let's say we start with this:

```
░░░░░░██░░░░
░░░░░░░░██░░
░░░░██████░░
░░░░░░░░░░░░
```
Remove the empty lines on the edges:

```
░░██░░
░░░░██
██████
```


No middle empty lines, square shape, so we need all 8 ones:

<table>
<thead><th>Picture</th><th><code>pixels</code></th><th>Picture</th><th><code>pixels</code></th></thead>
<tbody>

<tr>
<td>

```
░░██░░
░░░░██
██████
```

</td><td><code>010001111</code></td>
<td>

```
░░██░░
██░░░░
██████
```

</td><td><code>010100111</code></td>
</tr>

<tr>
<td>

```
░░████
██░░██
░░░░██
```

</td><td><code>011101001</code></td>
<td>

```
████░░
██░░██
██░░░░
```

</td><td><code>110101100</code></td>
</tr>

<tr>
<td>

```
██████
██░░░░
░░██░░
```

</td><td><code>111100010</code></td>
<td>

```
██████
░░░░██
░░██░░
```

</td><td><code>111001010</code></td>
</tr>

<tr>
<td>

```
██░░░░
██░░██
████░░
```

</td><td><code>100101110</code></td>
<td>

```
░░░░██
██░░██
░░████
```

</td><td><code>001101011</code></td>
</tr>

</tbody>
</table>

The last one, `001101011` is the minimal.

# Endpoints

If the things don't exist yet, or something else is wrong, return an `{"error" : {message}}`.

## `POST /pictures/create_all/{max_height}/{max_width}`

 - creates all Pictures up to the given size
 - adds a record for the minimal ones in the `Puzzles` table with `locally_solvable` as `null`
 - if a picture is already there, doesn't do anything
 - it can assume, that if any picture with size `n x m` is there, all of them, and all of the smaller ones are.

"Smaller" means a rotation can fit into it. 

For a the `/create_all/5/3` call these sizes are generated:
`5x3`,`5x2`,`5x1`,`4x3`,`4x2`,`4x1`,`3x5`,`3x4`,`3x2`,`3x1`,`2x5`,`2x4`,`2x2`,`2x1`,`1x5`,`1x4`,`1x2`,`1x1`,`0x0`.

Response is JSON:

```json
{
    "newly_generated_classes" : ["5x4","4x5"],
    "newly_created_pictures" : [id1,id2,...],
    "new_minimal_picture_count" : 12
}
```

## `GET /pictures/by_size/{height}/{width}`

JSON response:
```json
[id1,id2,...]
```

## `GET /pictures/by_size/minimal/{height}/{width}`

JSON response:
```json
[id1,id2,...]
```

## `GET /pictures/{id}`

```json
{
    "id" : id,
    "height" : height,
    "width" : width,
    "pixels" : pixels,
    "minimal" : minimal_id
}
```

## `GET /puzzles/size/{dim1}/{dim2}`

JSON response:
```json
{
    "height" : {min(dim1,dim2)},
    "width" : {max(dim1,dim2)},
    "puzzles" : [id1,id2,...]
}
```
## `GET /puzzles/{id}`

```json
{
    "picture_id" : id,
    "height" : height,
    "width" : width,
    "solution" : pixels,
    "clues" : {"rows" : [...], "columns" : [...]},
    "minimal_pictures_with_same_clues": [id, otherid1, otherid2],
    "locally_solvable" : true|false|null
}
```

## `POST /solve/{minimal_picture_id}`

If `locally_solvable` is `false`, immediately returns with `{"error" : "Puzzle known to be unsolvable"}` or something like that. 

If it is `true`, solve it, and post the results in the `Solutions` table, and return such a json:

```json
{
 "id" : id,
 "picture_id" : picture_id,
 "solution_time" : solution_time,
 "solver_name" : solver_name,
 "solver_version" : solver_version,
 "configuration" : configuration
}
```

If it is `null`, try to solve it, set the `locally_solvable` field.
If unsolvable `{"error" : "Puzzle not solvable"}`, otherwise do everything like in the `true` case.


## coming up...

There will be more, but for now these will suffice.


# Docker

Make a dockerfile, that puts your server/solver in an image, that listens on port 5000 for the above, which will be run like this:

```bash
docker run \
  -v db_config.json:db_config.json:ro \
  your-image
```

where `db_config.json` will be like this:

```json
{
    "host": "db",
    "port": 5432,
    "name": "nonogram",
    "user": "postgres",
    "password": "postgres"
}
```
