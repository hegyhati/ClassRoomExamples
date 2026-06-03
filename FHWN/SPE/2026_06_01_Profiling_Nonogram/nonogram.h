#include <vector>
#include <string>
#include <optional>

struct Clue {
    std::vector<int> sizes;

    Clue(std::vector<int> sizes) : sizes(sizes) {}
    Clue(std::string numbers) {
        int value = 0;
        for (unsigned int i = 0; i<numbers.size(); ++i) {
            if (numbers[i]==',') {
                sizes.push_back(value);
                value = 0;
            } else {
                value *= 10;
                value += (numbers[i]-'0');    
            }
        }
        sizes.push_back(value);
    }

    std::string toJSON() {
        std::string json = "[";
        for (unsigned int i = 0; i<sizes.size(); ++i) {
            if (i>0) json += ",";
            json += std::to_string(sizes[i]);
        }
        json += "]";
        return json;
    }

    bool operator==(const Clue& other) {
        if (other.sizes.size() != sizes.size()) return false;
        for (unsigned int i = 0; i < sizes.size(); ++i)
            if (sizes[i]!=other.sizes[i]) return false;
        return true;
    }
};

enum State{ UNKNOWN = '_', BLACK = '1', WHITE = '0' };
struct Line {
    std::vector<State> fields;

    Line(){}
    Line(int size) : fields(size,UNKNOWN) {};
    Line(std::string text) {
        for (char x: text)
            fields.push_back(State(x));
    }

    std::optional<Clue> getClues() {
        if (!isSolved()) return std::nullopt;
        int current = 0;
        std::vector<int> clues;
        for (State s : fields)
            if (s==BLACK) ++current;
            else if (current!=0) {
                clues.push_back(current);
                current = 0;
            }
        if (current!=0) clues.push_back(current);
        return Clue(clues);
    }
    
    std::string toSring() {
        std::string txt = "";
        for (State s : fields)
            txt += char(s);
        return txt;            
    }

    bool isSolved() {
        for (State s : fields)
            if (s == UNKNOWN) return false;
        return true;
    }

    std::vector<Line> allPossibleLines() {
        std::vector<Line> lines;
        if (isSolved()) {
            lines.push_back(*this);
            return lines;
        }
        bool first = true;
        for (unsigned int i = 0; i < fields.size(); ++i){
            if (fields[i] == UNKNOWN) {
                if (first) {
                    first = false;
                    Line tmp(*this);
                    tmp.fields[i] = BLACK;
                    lines.push_back(tmp);
                    tmp.fields[i] = WHITE;
                    lines.push_back(tmp);
                } else {
                    std::vector<Line> tmp_lines(lines);
                    lines.clear();
                    for (Line l: tmp_lines) {
                        l.fields[i] = BLACK;
                        lines.push_back(l);
                        l.fields[i] = WHITE;
                        lines.push_back(l);
                    }

                }
            }
        }
        return lines;
    }

    Line deduce(Clue clue) {
        std::vector<Line> lines = allPossibleLines();
        Line deduced;

        for(Line l: lines) {
            if (l.getClues().value() == clue) {
                if(deduced.fields.size() == 0) deduced = l;
                else 
                    for (unsigned int i = 0; i<fields.size(); ++i)
                        if (deduced.fields[i]!=l.fields[i])
                            deduced.fields[i] = UNKNOWN;
            }
        }
        return deduced;        
    }

};



