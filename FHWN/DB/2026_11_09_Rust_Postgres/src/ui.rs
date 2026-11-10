use std::fmt;
use std::io::{self, Write};
use postgres::Client;
use crate::peak::Peak;


impl fmt::Display for Peak {
    fn fmt(&self, formatter: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(
            formatter,
            "{} ({} m) @ {} ({},{})",
            self.name, self.elevation_meter, self.country, self.longitude, self.latitude
        )
    }
}

fn string_input(prompt: &str) -> String {
    print!("{}", prompt);
    io::stdout().flush().unwrap();
    let mut response : String = String::new();
    io::stdin().read_line(&mut response).unwrap();    
    response.trim().to_string()
}

fn number_input<T: std::str::FromStr>(prompt: &str) -> T {
    if let Ok(n) = string_input(prompt).parse::<T>() {
        return n;
    }

    loop {
        if let Ok(n) = string_input("Must be a number, try again: ").trim().parse::<T>() {
            break n;
        }
    }
}

fn yes_no_question(prompt: &str) -> bool {
    let mut answer = string_input(&format!("{} (Y/N) ",prompt));
    loop {
        match answer.as_str() {
            "y" | "Y" | "yes" | "Yes" => break true ,
            "n" | "N" | "no"  | "No"  => break false,
            _ => answer = string_input("Answer with Y or N: "),
        }
    }   
}

fn list_peaks_above_elavation(client: &mut Client, elavation_meter: i16) {
    if let Ok(peaks) =  Peak::get_peaks_above(client, elavation_meter) {
        for peak in peaks {
            println!(" - {}", &peak);
        } 
    } else {
        println!("Sorry, could not fetch the peaks...");
    }
}

fn input_new_peak(client: &mut Client) {
    match (Peak {
        id: None,
        name: string_input("What is the name of the peak? "),
        country: string_input("In which country is this peak located? "),
        elevation_meter: number_input::<i16>("What is the elevation? "),
        longitude:  number_input::<f32>("Longitude: "),
        latitude: number_input::<f32>("Latitude: "),
        climbing_equipment_needed: yes_no_question("Do you need special hiking equipment to climb it? ")
    }.persist_peak(client)) {
        Ok(_) => println!("Peak successfully added to the database."),
        Err(_) => println!("There was a problem adding the peak to the database."),
    }
}

pub fn main_menu(client: &mut Client) {
    loop {
        match string_input("
            What do you want do do?
                1. List all peaks.
                2. List peaks above an elavation.
                3. Add new peak.
                4. Exit
        ").as_str() {
            "1" => { list_peaks_above_elavation(client,0); }
            "2" => { 
                let elevation = loop {
                    let input = number_input::<i16>("Enter the lower limit for the elavation in meters: ");
                    if input > 0 { break input as i16; } else { println!("Elavation must be a number."); }
                };
                list_peaks_above_elavation(client, elevation);
            }
            "3" => { input_new_peak(client); }
            "4" => { println!("Bye-bye."); return; }
            _ => { println!("Sorry, wrong command."); }
        }
    }
}