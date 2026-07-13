package com.example.hibernate;

import org.junit.jupiter.api.Test;

import java.time.LocalDate;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertTrue;

class PatientVisitTest {

    @Test
    void patientConstructorInitializesSsnAndEmptyVisits() {
        Patient patient = new Patient("Test Patient", "1111", "Test Address");

        assertEquals("1111", patient.getSsn());
        assertNotNull(patient.getVisits());
        assertTrue(patient.getVisits().isEmpty());
    }

    @Test
    void visitConstructorAssignsPatient() {
        Patient patient = new Patient("Another Patient", "2222", "Another Address");
        Visit visit = new Visit(LocalDate.of(2026, 6, 18), "check-up", patient);
        patient.addVisit(visit);

        assertEquals(patient, visit.getPatient());
        assertEquals(1,patient.getVisits().size());
    }
} 
