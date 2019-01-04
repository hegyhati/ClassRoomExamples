#ifndef TEXT_H
#define TEXT_H

#include <string>
#include "treenode.h"

class Text : public TreeNode
{
    std::string content;
public:
    Text(std::string content="");
    std::string toHTML();
};

#endif // TEXT_H
