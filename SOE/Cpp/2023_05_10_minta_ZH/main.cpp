#include <algorithm>
#include <cmath>
#include <fstream>
#include <iostream>
#include <ostream>
#include <vector>

constexpr double pi = 3.14159265358979323846;


union Point2D {
  struct {
    const double x;
    const double y;
  };
  const double pos[2];
  friend std::ostream &operator<<(std::ostream &os, const Point2D &p) {
    return os << '(' << p.x << ',' << p.y << ')';
  }
};

class PolyLine : private std::vector<Point2D> {
  double select_extrema(bool smaller, unsigned int dimension) const {
    return std::min_element(begin(), end(),
                            [=](const Point2D &p1, const Point2D &p2) {
                              return smaller ==
                                     (p1.pos[dimension] < p2.pos[dimension]);
                            })
        ->pos[dimension];
  }

public:
  void reset() { clear(); }
  void append(const Point2D &p) { push_back(p); }
  double min_x() const { return select_extrema(true, 0); }
  double min_y() const { return select_extrema(true, 1); }
  double max_x() const { return select_extrema(false, 0); }
  double max_y() const { return select_extrema(false, 1); }

  friend std::ostream &operator<<(std::ostream &os, const PolyLine &pl) {
    for (const Point2D &p : pl)
      os << p << " ";
    return os;
  }
  void saveToSVG(std::string filename, const int border = 20,
                 bool mirror = true) {
    std::ofstream svgFile(filename);
    svgFile << "<svg xmlns=\"http://www.w3.org/2000/svg\" viewbox=\""
            << min_x() - border << " " << min_y() - border << " "
            << max_x() - min_x() + 2 * border << " "
            << max_y() - min_y() + 2 * border << "\">\n";
    for (unsigned int i = 1; i < size(); ++i) {
      svgFile << "\t<line "
              << "x1=\"" << at(i - 1).x << "\" y1=\""
              << (mirror ? max_y() - at(i - 1).y : at(i - 1).y) << "\" "
              << "x2=\"" << at(i).x << "\" y2=\""
              << (mirror ? max_y() - at(i).y : at(i).y) << "\" "
              << "stroke=\"black\" />\n";
    }
    svgFile << "</svg>\n";
    svgFile.close();
  }
};

int main() {
  PolyLine pl;

  std::ifstream code("house.logo");

  double x = 0, y = 0, alpha = pi / 2;
  pl.append({x, y});

  while (!code.eof()) {
    std::string command;
    double argument;
    code >> command >> argument;
    if (command == "fd") {
      x += argument * cos(alpha);
      y += argument * sin(alpha);
    } else if (command[1] == 't') {
      alpha += argument * pi / 180 * (command[0] == 'r' ? -1 : 1);
    }
    pl.append({x, y});
  }
  code.close();
  pl.saveToSVG("house.svg");
  return 0;
}
