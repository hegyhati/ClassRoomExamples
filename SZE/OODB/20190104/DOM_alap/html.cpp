#include "html.h"

HTML::HTML():root(new Tag("html"))
{
    root->appendChild(new Tag("head"));
    root->appendChild(new Tag("body","body"));
}

HTML::~HTML()
{
    delete root;
}

void HTML::addElement(TreeNode *element)
{
    root->getById("body")->appendChild(element);
}

Tag *HTML::getTagById(std::string id)
{
    return root->getById(id);
}

std::ostream &operator<<(std::ostream &o, const HTML &html)
{
    o << html.root->toHTML();
    return o;
}
