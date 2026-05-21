package com.example.hibernate;

import org.hibernate.Session;
import org.hibernate.Transaction;

import java.io.File;
import java.time.LocalDate;
import java.util.List;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        if (!new File("patients.db").exists())
            DatabaseSeeder.seed();

        Scanner scanner = new Scanner(System.in);
        boolean running = true;

        while (running) {
            System.out.println("\n=== Patient Registry ===");
            System.out.println("1. List all patients");
            System.out.println("2. Add new patient");
            System.out.println("3. List visits for a patient");
            System.out.println("4. Add visit for a patient");
            System.out.println("0. Exit");
            System.out.print("Choice: ");

            String choice = scanner.nextLine().trim();
            switch (choice) {
                case "1" -> listPatients();
                case "2" -> addPatient(scanner);
                case "3" -> listVisits(scanner);
                case "4" -> addVisit(scanner);
                case "0" -> running = false;
                default  -> System.out.println("Unknown option.");
            }
        }

        HibernateUtil.shutdown();
    }

    private static void listPatients() {
        try (Session session = HibernateUtil.getSessionFactory().openSession()) {
            List<Patient> patients = session.createQuery("FROM Patient ORDER BY name", Patient.class).list();
            System.out.println("\n--- Patients (" + patients.size() + ") ---");
            patients.forEach(System.out::println);
        }
    }

    private static void addPatient(Scanner scanner) {
        System.out.print("Name: ");
        String name = scanner.nextLine().trim();
        System.out.print("SSN: ");
        String ssn = scanner.nextLine().trim();
        System.out.print("Address: ");
        String address = scanner.nextLine().trim();

        Patient patient = new Patient(name, ssn, address);
        try (Session session = HibernateUtil.getSessionFactory().openSession()) {
            Transaction tx = session.beginTransaction();
            session.persist(patient);
            tx.commit();
            System.out.println("Saved: " + patient);
        }
    }

    private static void listVisits(Scanner scanner) {
        System.out.print("Patient SSN: ");
        String ssn = scanner.nextLine().trim();
        try (Session session = HibernateUtil.getSessionFactory().openSession()) {
            Patient patient = session.createQuery(
                "FROM Patient p WHERE p.ssn = :ssn", Patient.class)
                .setParameter("ssn", ssn).uniqueResult();
            if (patient == null) {
                System.out.println("No patient found with SSN: " + ssn);
                return;
            }
            List<Visit> visits = session.createQuery(
                "FROM Visit v WHERE v.patient = :p ORDER BY v.date", Visit.class)
                .setParameter("p", patient).list();
            System.out.println("\n--- Visits for " + patient + " (" + visits.size() + ") ---");
            if (visits.isEmpty()) System.out.println("  (none)");
            else visits.forEach(System.out::println);
        }
    }

    private static void addVisit(Scanner scanner) {
        System.out.print("Patient SSN: ");
        String ssn = scanner.nextLine().trim();
        try (Session session = HibernateUtil.getSessionFactory().openSession()) {
            Patient patient = session.createQuery(
                "FROM Patient p WHERE p.ssn = :ssn", Patient.class)
                .setParameter("ssn", ssn).uniqueResult();
            if (patient == null) {
                System.out.println("No patient found with SSN: " + ssn);
                return;
            }
            System.out.print("Date (YYYY-MM-DD): ");
            LocalDate date = LocalDate.parse(scanner.nextLine().trim());
            System.out.print("Reason: ");
            String reason = scanner.nextLine().trim();

            Visit visit = new Visit(date, reason, patient);
            Transaction tx = session.beginTransaction();
            session.persist(visit);
            tx.commit();
            System.out.println("Saved:" + visit);
        }
    }
}
