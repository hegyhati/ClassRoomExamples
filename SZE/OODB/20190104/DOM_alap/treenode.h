#ifndef TREENODE_H
#define TREENODE_H

#include <string>

class TreeNode
{
public:
    virtual std::string toHTML() =0;
    virtual ~TreeNode(){}
};

#endif // TREENODE_H
