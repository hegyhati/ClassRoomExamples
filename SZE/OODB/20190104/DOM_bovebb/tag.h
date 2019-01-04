#ifndef TAG_H
#define TAG_H

#include "treenode.h"
#include <string>
#include <map>
#include <list>

class Tag : public TreeNode
{
    std::string name;
    std::map<std::string,std::string> attributes;
    std::list<TreeNode*> children;
public:
    Tag(std::string name, std::string id="");
    virtual ~Tag();
    virtual std::string toHTML() const override;
    bool hasAttribute(std::string name) const;
    std::string getAttribute(std::string name) const;
    void setAttribute(std::string name, std::string value);
    bool isId(std::string id) const;
    Tag* getById(std::string id);
    void appendChild(TreeNode* child);

};

#endif // TAG_H
