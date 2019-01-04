#include "tag.h"

Tag::Tag(std::string name, std::string id) : name (name)
{
    if(id!="") attributes["id"]=id;
}

Tag::~Tag()
{
    for(auto& child:children)
        delete child;
}

std::string Tag::toHTML() const
{
    std::string toReturn="";
    toReturn+="<"+name;
    for(const auto& attr: attributes)
        toReturn+=" "+attr.first+"="+"\""+attr.second+"\"";
    toReturn+=">";
    for(const auto& element: children)
        toReturn+=element->toHTML();
    toReturn+="</"+name+">";
    return toReturn;
}

bool Tag::hasAttribute(std::string name) const
{
    return attributes.find(name)!=attributes.end();
}

void Tag::setAttribute(std::string name, std::string value)
{
    attributes[name]=value;
}

bool Tag::isId(std::string id) const
{
    if(attributes.find("id")==attributes.end()) return false;
    else return attributes.at("id")==id;
}

Tag *Tag::getById(std::string id)
{
    if(isId(id)) return this;

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

std::string Tag::getAttribute(std::string name) const
{
    if(hasAttribute(name)) return attributes.at(name);
    else return "";
}

