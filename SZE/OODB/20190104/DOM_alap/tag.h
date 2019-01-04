#ifndef TAG_H
#define TAG_H

#include "treenode.h"
#include <string>
#include <map>
#include <list>

class Tag : public TreeNode
{
    std::string name;
    std::string id;
    std::list<TreeNode*> children;
public:
    Tag(std::string name, std::string id="");
    virtual ~Tag();
    virtual std::string toHTML();
    bool isId(std::string id);
    Tag* getById(std::string id);
    void appendChild(TreeNode* child);

};

#endif // TAG_H
