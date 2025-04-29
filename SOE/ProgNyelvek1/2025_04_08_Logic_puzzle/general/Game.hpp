#pragma once

#include <map> 
#include <algorithm>
#include <ranges>
#include "Person.hpp"
#include "Rule.hpp"

class Game {
public: 
    struct GameState{
        const People leftBank;
        const People rightBank;
        const bool boat_left;

        const People& currentBank() const { return boat_left ? leftBank : rightBank; }
        const People& otherBank() const {return boat_left ? rightBank : leftBank; }
        
        GameState applyMove(const People& boat) { // without checks, maybe throw exception if not isBoatValid
            People newLeftBank, newRightBank;
            auto [oldFrom, oldTo, newFrom, newTo] = boat_left ? 
                std::tuple{leftBank, rightBank, newLeftBank, newRightBank} :
                std::tuple{rightBank, leftBank, newRightBank, newLeftBank};
            
            std::set_difference( oldFrom.begin(), oldFrom.end(), boat.begin(), boat.end(),
                std::inserter(newFrom, newFrom.begin()));
            std::set_union( oldTo.begin(), oldTo.end(), boat.begin(), boat.end(),
                std::inserter(newTo, newTo.begin()));

            return GameState{newLeftBank, newRightBank, !boat_left};
        }

        bool isBoatValid(const People& boat) const {
            const People& fromBank = currentBank();
            for (const auto& person: boat)
                if (!fromBank.contains(person)) return false;
            return true;
        }
    };

private:
    std::map<std::string, std::shared_ptr<Person>> people;
    std::set<std::unique_ptr<Rule>> bankRules;
    std::set<std::unique_ptr<Rule>> boatRules;

public:

    bool addPerson(Person&& person){
        if (people.contains(person.name)) return false;
        people[person.name] = std::make_shared<Person>(person);
        return true;
    }

    template <typename DerivedRule>
    void addBoatRule(DerivedRule&& rule) {
        boatRules.emplace(std::make_unique<DerivedRule>(rule));
    }
    
    template <typename DerivedRule>
    void addBankRule(DerivedRule&& rule) {
        bankRules.emplace(std::make_unique<DerivedRule>(rule));
    }

    GameState initialState() const {
        return GameState {
            People{std::views::values(people).begin(), std::views::values(people).end()},
            People(),
            true
        };
    }

    bool isStateValid(const GameState& state) const {
        for (const auto& rule: bankRules) {
            if (!(*rule)(state.leftBank)) return false;
            if (!(*rule)(state.rightBank)) return false;
        }
        return true;
    }

    bool isBoatValid(const People& boat, const GameState& state) const {
        if (!state.isBoatValid(boat)) return false;
        for (const auto& rule: boatRules) 
            if (!(*rule)(boat)) return false;
        return true;
    }

    People getBoatByNames(const std::set<std::string>& names) {
        People boat;
        for (const auto& name: names)
            if (people.contains(name)) // maybe throw exception if not
                boat.insert(people[name]);
        return boat;
    }
};