#ifndef TEXT_H
#define TEXT_H

#include <string>
#include "treenode.h"

class Text : public TreeNode
{
    std::string content;
public:
    Text(std::string content="");
    std::string toHTML() const override;
    std::string getContent() const;
    void setContent(const std::string &value);
};

#endif // TEXT_H
