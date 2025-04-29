#pragma once

#include "Person.hpp"
#include <memory>

using People = std::set<std::shared_ptr<Person>>;

struct Rule {
    virtual bool operator()(const People& people) const = 0;
};


struct AtLeastOneOfRule : public Rule {
    const std::set<std::string> names;
    AtLeastOneOfRule(std::set<std::string> names) : names(names){}
    bool operator()(const People& people) const override {
        for (const auto& person: people) 
            if (names.contains(person->name)) return true;
        return false;
    }
};

struct AtLeastOneWithLabelRule : public Rule {
    const std::string label;
    AtLeastOneWithLabelRule(std::string label) : label(label) {}
    bool operator()(const People& people) const override {
        for (const auto& person: people) 
            if (person->hasLabel(label)) return true;
        return false;
    }
};

struct AtMostNRule : public Rule {
    const unsigned int max_count;
    AtMostNRule(unsigned int max_count) : max_count(max_count) {}
    bool operator()(const People& people) const override {
        return people.size() <= max_count;
    }
};


