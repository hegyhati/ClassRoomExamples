CREATE TABLE pictures (
	id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	height INTEGER NOT NULL CHECK (height >= 0),
	width INTEGER NOT NULL CHECK (width >= 0),
	pixels BYTEA NOT NULL,
	smallest_equivalent_id BIGINT NOT NULL,
	CONSTRAINT uq_pictures_height_width_pixels UNIQUE (height, width, pixels),
	CONSTRAINT fk_pictures_smallest_equivalent
		FOREIGN KEY (smallest_equivalent_id) REFERENCES pictures(id)
);

CREATE TABLE puzzles (
	picture_id BIGINT PRIMARY KEY,
	clues JSONB NOT NULL,
	locally_solvable BOOLEAN NULL,
	CONSTRAINT fk_puzzles_picture
		FOREIGN KEY (picture_id) REFERENCES pictures(id)
);

CREATE TABLE solutions (
	picture_id BIGINT NOT NULL,
	solution_time INTEGER NOT NULL CHECK (solution_time >= 0),
	solver_name TEXT NOT NULL CHECK (solver_name IN ('Bun', 'Node', 'Java', 'c#')),
	solver_version INTEGER NOT NULL CHECK (solver_version >= 0),
	configuration JSONB NOT NULL,
	CONSTRAINT fk_solutions_picture
		FOREIGN KEY (picture_id) REFERENCES pictures(id)
);
