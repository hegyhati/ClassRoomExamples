#include <cmath>
#include <fstream>
#include <iostream>
#include <vector>

const double pi = 3.14159265358979323846;

struct Point2D {
  const double x;
  const double y;
};

class PolyLine {
  std::vector<Point2D> points;
  double minx, miny, maxx, maxy;

public:
  PolyLine() { points.clear(); }
  void reset() {
    points.clear();
    minx = miny = maxx = maxy = 0;
  }
  void append(const Point2D &p) {
    if (points.size() == 0) {
      minx = maxx = p.x;
      miny = maxy = p.y;
    } else {
      if (p.x < minx) minx = p.x;
      else if (p.x > maxx) maxx = p.x;
      if (p.y < miny) miny = p.y;
      else if (p.y > maxy) maxy = p.y;
    }
    points.push_back(p);
  }

  void saveToSVG(std::string filename, const int border = 20) {
    std::ofstream svgFile(filename);
    svgFile << "<svg xmlns=\"http://www.w3.org/2000/svg\" viewbox=\""
            << minx - border << " " << miny - border << " "
            << maxx - minx + 2 * border << " " << maxy - miny + 2 * border
            << "\">\n";
    for (unsigned int i = 1; i < points.size(); ++i) {
      svgFile << "\t<line "
              << "x1=\"" << points[i - 1].x << "\" y1=\"" << points[i - 1].y
              << "\" "
              << "x2=\"" << points[i].x << "\" y2=\"" << points[i].y << "\" "
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
      y -= argument * sin(alpha);
    } else if (command == "rt") {
      alpha -= argument * pi / 180;
    } else if (command == "lt") {
      alpha -= argument * pi / 180;
    }
    pl.append(Point2D{x, y});
  }
  code.close();
  pl.saveToSVG("house_simpler.svg");
  return 0;
}
