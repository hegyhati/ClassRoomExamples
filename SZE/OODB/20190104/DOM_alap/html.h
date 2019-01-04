#ifndef HTML_H
#define HTML_H

#include "tag.h"
#include <string>
#include <iostream>




class HTML
{
    Tag* const root;
public:

    HTML();
    ~HTML();

    friend std::ostream& operator<< (std::ostream& o, const HTML& html);
    void addElement(TreeNode* element);
    Tag* getTagById(std::string id);
};


#endif // HTML_H
