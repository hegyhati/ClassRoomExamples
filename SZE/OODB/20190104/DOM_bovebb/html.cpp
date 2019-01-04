#include "html.h"

HTML::HTML(std::string lang)
    :root(new Tag("html")),head(new Tag("head")),body(new Tag("body"))
{
    root->setAttribute("lang",lang);
    root->appendChild(head);
    root->appendChild(body);
}

HTML::~HTML()
{
    delete root;
}

void HTML::addElement(TreeNode *element)
{
    body->appendChild(element);
}

Tag *HTML::getTagById(std::string id)
{
    Tag* toReturn = body->getById(id);
    if (toReturn==nullptr) throw IdNotFound({id});
    else return toReturn;
}


std::ostream &operator<<(std::ostream &o, const HTML &html)
{
    o << html.root->toHTML();
    return o;
}
