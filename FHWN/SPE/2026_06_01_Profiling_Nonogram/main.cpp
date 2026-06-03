#include "httplib.h"
#include <iostream>
#include "nonogram.h"



int main() {
    httplib::Server server;

    server.Get("/hello", [](const httplib::Request&, httplib::Response& res) {
        res.set_content("Hello from C++!", "text/plain");
    });

    server.Get(R"(/line2clue/(.+))", [](const httplib::Request& req, httplib::Response& res) {
        auto clues = Line(req.matches[1]).getClues();
        res.set_content(
            clues 
                ? clues.value().toJSON()
                : "{ \"error\" : \"Line is not complete.\"}"
            , "application/json"
        );
    });

    server.Get(R"(/txt2clue/(.+))", [](const httplib::Request& req, httplib::Response& res) {
        auto clues = Clue(req.matches[1]);
        res.set_content(clues.toJSON(), "application/json");
    });

    server.Get(R"(/lines4line/(.+))", [](const httplib::Request& req, httplib::Response& res) {
        auto lines = Line(req.matches[1]).allPossibleLines();
        std::string response = "[";
        for( unsigned int i = 0; i<lines.size(); ++i) {
            if (i>0) response += ",";
            response += "\"" + lines[i].toSring() + "\"";
        }
        response += "]";
        res.set_content(response, "application/json");
    });

    server.Get(R"(/deduce/(.+)/(.+))", [](const httplib::Request& req, httplib::Response& res) {
        auto line = Line(req.matches[1]);
        auto clue = Clue(req.matches[2]);
        res.set_content("\"" + line.deduce(clue).toSring() + "\"", "application/json");
    });

    std::cout << "Server running on http://localhost:8080\n";

    server.listen("0.0.0.0", 8080);
}