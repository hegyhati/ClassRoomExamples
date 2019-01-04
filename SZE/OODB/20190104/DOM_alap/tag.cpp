#include "tag.h"

Tag::Tag(std::string name, std::string id) : name (name), id (id) {}

Tag::~Tag()
{
    for(auto& child:children)
        delete child;
}

std::string Tag::toHTML() 
{
    std::string toReturn="<"+name+" id=\"" + id + "\">";
    for(const auto& element: children)
        toReturn+=element->toHTML();
    toReturn+="</"+name+">";
    return toReturn;
}

Tag *Tag::getById(std::string id)
{
    if(this->id==id) return this;

    for(auto& child:children)
    {
        Tag* tagChild=dynamic_cast<Tag*>(child);
        if(tagChild!=nullptr)
        {
            Tag* toReturn=tagChild->getById(id);
            if (toReturn!=nullptr) return toReturn;
        }
    }
    return nullptr;
}

void Tag::appendChild(TreeNode *child)
{
    children.push_back(child);
}
