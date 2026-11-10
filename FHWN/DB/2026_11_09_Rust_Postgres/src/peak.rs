use postgres::{Client, Error, Row};

pub struct Peak {
    pub id: Option<i32>,
    pub name: String,
    pub country: String,
    pub elevation_meter: i16,
    pub longitude: f32,
    pub latitude: f32,
    pub climbing_equipment_needed: bool
}


impl Peak {
    pub fn initialize_table(client: &mut Client) -> Result<(), Error> {
        client.batch_execute("
            CREATE TABLE IF NOT EXISTS Peaks (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL CHECK (length(trim(name)) > 0),
                country TEXT NOT NULL CHECK (length(trim(country)) > 0),
                elevation_meter SMALLINT NOT NULL CHECK (elevation_meter > 0),
                longitude REAL NOT NULL CHECK (longitude BETWEEN -180 AND 180),
                latitude REAL NOT NULL CHECK (latitude BETWEEN -90 AND 90),
                climbing_equipment_needed BOOL NOT NULL
            );

            INSERT INTO Peaks (name, country, elevation_meter, longitude, latitude, climbing_equipment_needed)
            SELECT seed.name, seed.country, seed.elevation_meter, seed.longitude, seed.latitude, seed.climbing_equipment_needed
            FROM (VALUES
                ('Mount Everest', 'Nepal/China', 8849, 86.9250, 27.9881, TRUE),
                ('K2', 'Pakistan/China', 8611, 76.5158, 35.8808, TRUE),
                ('Nanga Parbat', 'Pakistan', 8126, 74.5892, 35.2375, TRUE),
                ('Annapurna I', 'Nepal', 8091, 83.8203, 28.5958, TRUE),
                ('Schneeberg', 'Austria', 2076, 15.8040, 47.7670, FALSE),
                ('Geschriebenstein / Írott-kő', 'Austria/Hungary', 884, 16.4330, 47.3510, FALSE),
                ('Kőris-hegy', 'Hungary', 709, 17.8860, 46.9820, FALSE),
                ('Poloskás-bérc (Sopron)', 'Hungary', 557, 16.5660, 47.6810, FALSE),
                ('Devínska Kobyla', 'Slovakia', 514, 17.0100, 48.1900, FALSE)
            ) AS seed(name, country, elevation_meter, longitude, latitude, climbing_equipment_needed)
            WHERE NOT EXISTS (
                SELECT 1 FROM Peaks WHERE Peaks.name = seed.name
            );
        ")
    }

    pub fn persist_peak(&self, client: &mut Client) -> Result<u64,Error> {
        if let Some(id) = self.id {
            client.execute("
                    UPDATE Peaks
                    SET name = $1, country = $2, elevation_meter = $3, longitude = $4, latitude = $5, climbing_equipment_needed = $6
                    WHERE id = $7
                ", &[&self.name, &self.country, &self.elevation_meter, &self.longitude, &self.latitude, &self.climbing_equipment_needed, &id],
            )
        } else {
            client.execute("
                    INSERT INTO Peaks (name, country, elevation_meter, longitude, latitude, climbing_equipment_needed)
                    VALUES ($1,$2,$3,$4,$5,$6);
                ", &[&self.name, &self.country, &self.elevation_meter, &self.longitude, &self.latitude, &self.climbing_equipment_needed]
            )
        }
    }

    fn fetch_from_row(row: &Row) -> Peak {
        Peak {
            id: Some(row.get("id")),
            name: row.get("name"),
            country: row.get("country"),
            elevation_meter: row.get("elevation_meter"),
            longitude: row.get("longitude"),
            latitude: row.get("latitude"),
            climbing_equipment_needed: row.get("climbing_equipment_needed"),
        }
    }

    pub fn get_peaks_above(client: &mut Client, elevation_meter: i16) -> Result<Vec<Peak>, Error> {
        let rows = client.query(
            "SELECT * FROM Peaks WHERE elevation_meter >= $1",
            &[&elevation_meter],
        )?;

        let mut peaks = Vec::new();
        for row in rows {
            peaks.push(Peak::fetch_from_row(&row));
        }

        Ok(peaks)
    }

}


