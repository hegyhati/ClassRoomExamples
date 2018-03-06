#ifndef TESTER_HPP
#define TESTER_HPP

#include <iostream>
using namespace std;

#define INITIAL_DEFAULTMAXD 1

struct Step {
    int dx;
    int dy;
    struct Step * next;
};


class Tester {
        static int defaultmaxd;
        const int maxd;
        const int width;
        const int height;
        int x;
        int y;
        struct Step * steps;
        bool isCorrectNextStep(int dx, int dy) const;
        struct Step * getLastStep() const;
    public:
        Tester(int wsidth, int height, int maxd=defaultmaxd);
        ~Tester();
        void print() const;
        void fancyPrint() const;
        bool isFinished() const;
        bool isGameOver() const;
        bool move(int dx, int dy);
        void static setDefaultMaxD(int newmaxd);
};

#endif
