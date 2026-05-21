package com.example.hibernate;

import jakarta.persistence.CascadeType;
import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.OneToMany;
import jakarta.persistence.Table;

import java.util.ArrayList;
import java.util.List;

@Entity
@Table(name = "patients")
public class Patient {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private String name;

    @Column(nullable = false, unique = true)
    private String ssn;

    @Column
    private String address;

    @OneToMany(mappedBy = "patient", cascade = CascadeType.ALL, fetch = FetchType.LAZY)
    private List<Visit> visits = new ArrayList<>();

    public Patient(){}

    public Patient(String name, String ssn, String address) {
        this.name = name;
        this.ssn = ssn;
        this.address = address;
    }

    public String getSsn() { return ssn; }
    public List<Visit> getVisits() { return visits; }

    @Override
    public String toString() {
        return String.format("[%d] %-25s SSN: %-6s  Address: %s", id, name, ssn, address);
    }
}
