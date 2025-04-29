#pragma once

#include <string>
#include <set>

struct Person {
    const std::string name;
    const std::set<std::string> labels;

    Person( const std::string& name, const std::set<std::string>& labels)
        :name(name), labels(labels) {}

    std::string to_string() const {
        return name; // TODO add labels in braces
    }

    bool hasLabel(const std::string& label) const { return labels.contains(label); }
};



