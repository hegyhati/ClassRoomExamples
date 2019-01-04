#include <iostream>
#include "html.h"
#include "tag.h"
#include "text.h"
#include <string>
#include <list>
#include <fstream>

using namespace std;

int main(int argc, char** argv)
{
    HTML test("hu");

    try
    {
        test.addElement(new Tag("h1","title"));
        test.getTagById("title")->appendChild(new Text("Szükséges feltételek OODB vizsgán"));
        test.addElement(new Tag("ul","requirements"));
        const list<string> requirements ({
                                             "A kód csak standard C++11 elemeket használjon.",
                                             "A kód warning nélkül forduljon le --Wall kapcsoló mellett is.",
                                             "A bináris ne szemeteljen a memóriába.",
                                             "A bináris semmilyen bemenet esetén nem segfaultolhat el."
                                         });
        for(const auto& req: requirements)
        {
            Tag* item=new Tag("li");
            item->appendChild(new Text(req));
            test.getTagById("requirements")->appendChild(item);
        }
        test.addElement(new Text("Megj.: A fenti feltételek csak szükségesek, de nem elégségesek a kettes szintjének eléréséhez."));
        cout<<test;
        string filename;
        if(argc==1) filename="index.html";
        else filename=argv[1];

        ofstream output(filename);
        if(output.is_open())
        {
            output<<test;
            output.close();
        }
    }
    catch (HTML::IdNotFound e)
    {
        cerr<<"Sorry, no element with id \""<<e.id<<"\" was found."<<endl;
    }

    return 0;
}

