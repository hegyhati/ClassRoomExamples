#include <string>
#include <list>
#include <iostream>
#include <sstream>

using namespace std;

class TreeNode {
  public:
    virtual string toHTML() const =0;
};

class Text:public TreeNode{
    string text;
  public:
    Text(string text):text(text){}
     string toHTML() const override {return text;}
};


class Tag: public TreeNode{
    string tagname;
    string id;
    list<TreeNode*> children;
  public:
    Tag(string tagname, string id): tagname(tagname), id(id){}
    ~Tag(){
      for(auto& child:children)
        delete child;
    }
    void appendChild(TreeNode* newchild) {
      children.push_back(newchild);
    }
    string toHTML() const override{
      stringstream ss;
      ss << "<" << tagname << " id='" << id << "'>" << endl;
      for(auto& child:children)
        ss << child->toHTML();
      ss << "</" << tagname << ">" << endl;
      return ss.str();
    }
    Tag* getById(string id){
      if(this->id == id) return this;
      Tag* tmp;
      Tag* tmpchild;
      for(auto& child:children) {
        tmpchild=dynamic_cast<Tag*>(child);
        if (tmpchild) {
          tmp=tmpchild->getById(id);
          if(tmp!=nullptr) return tmp;
        }
      }
      return nullptr;      
    }

};


class HTML{
    Tag html;
  public:
    HTML():html("html","myhtml"){
      html.appendChild( new Tag("head","myhead"));
      html.appendChild( new Tag("body","body"));
    }
    Tag* getTagById(string id){
      return html.getById(id);
    }
    void addElement(TreeNode* newelement) {
      html.getById("body")->appendChild(newelement);
    }
    string toHTML(){return html.toHTML();}
      
};


int main(){
    HTML test;
    
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
        Tag* item=new Tag("li","lista");
        item->appendChild(new Text(req));
        test.getTagById("requirements")->appendChild(item);
    }
    
    test.addElement(new Text("Megj.: A fenti feltételek csak szükségesek, de nem elégségesek a kettes szintjének eléréséhez."));

    cout << test.toHTML();  
}

