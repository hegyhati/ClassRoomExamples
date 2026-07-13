package com.example.hibernate;

import org.hibernate.Session;
import org.hibernate.Transaction;

import java.time.LocalDate;
import java.util.List;
import java.util.Map;

public class DatabaseSeeder {

    private static final List<Patient> INITIAL_PATIENTS = List.of(
        new Patient("Bilbo Baggins",       "1234", "Bag End, Shire"),
        new Patient("Frodo Baggins",       "5678", "Bag End, Shire"),
        new Patient("Gandalf the Grey",    "9012", "Wizard Tower, Grey Mountains"),
        new Patient("Aragorn Strider",     "3456", "Weathertop, Misty Mountains"),
        new Patient("Legolas Greenleaf",   "7890", "Mirkwood Forest, Woodland Realm"),
        new Patient("Gimli Lockbeard",     "1357", "Khazad-dûm, Dwarf Kingdom"),
        new Patient("Boromir of Gondor",   "2468", "Minas Tirith, Gondor"),
        new Patient("Samwise Gamgee",      "3579", "Hobbiton, Shire"),
        new Patient("Meriadoc Brandybuck", "4680", "Buckland, Shire"),
        new Patient("Peregrin Took",       "5791", "Great Smials, Shire"),
        new Patient("Gollum Sméagol",      "6802", "Misty Mountains, Goblin Tunnels")
    );

    // SSN -> list of [date, reason] pairs
    private static final Map<String, List<String[]>> INITIAL_VISITS = Map.of(
        "1234", List.of(
            new String[]{"2025-02-24", "hallucinations"},
            new String[]{"2025-02-24", "hallucinations"},
            new String[]{"2025-02-24", "hallucinations"}
        ),
        "5678", List.of(
            new String[]{"2025-02-20", "anxiety"},
            new String[]{"2025-03-02", "headache"},
            new String[]{"2025-03-10", "check-up"}
        ),
        "9012", List.of(
            new String[]{"2025-02-18", "fatigue"},
            new String[]{"2025-02-28", "arthritis pain"},
            new String[]{"2025-03-08", "follow-up"}
        ),
        "3456", List.of(
            new String[]{"2025-02-22", "wound care"},
            new String[]{"2025-03-04", "infection check"},
            new String[]{"2025-03-14", "physical therapy"}
        ),
        "7890", List.of(
            new String[]{"2025-02-25", "vision check"},
            new String[]{"2025-03-06", "eye strain"},
            new String[]{"2025-03-13", "glasses adjustment"}
        ),
        "1357", List.of(
            new String[]{"2025-02-19", "back injury"},
            new String[]{"2025-03-03", "physical therapy"},
            new String[]{"2025-03-11", "progress review"}
        ),
        "2468", List.of(
            new String[]{"2025-02-21", "muscle strain"},
            new String[]{"2025-02-28", "treatment"},
            new String[]{"2025-03-09", "follow-up"}
        )
    );

    public static void seed() {
        try (Session session = HibernateUtil.getSessionFactory().openSession()) {
            Transaction tx = session.beginTransaction();
            INITIAL_PATIENTS.forEach(session::persist);
            tx.commit();
            System.out.println("Database seeded with " + INITIAL_PATIENTS.size() + " patients.");

            tx = session.beginTransaction();
            int total = 0;
            for (var entry : INITIAL_VISITS.entrySet()) {
                String ssn = entry.getKey();
                Patient patient = session.createQuery(
                    "FROM Patient p WHERE p.ssn = :ssn", Patient.class)
                    .setParameter("ssn", ssn).uniqueResult();
                if (patient == null) continue;
                for (String[] v : entry.getValue()) {
                    session.persist(new Visit(LocalDate.parse(v[0]), v[1], patient));
                    total++;
                }
            }
            tx.commit();
            System.out.println("Database seeded with " + total + " visits.");
        }
    }
}
