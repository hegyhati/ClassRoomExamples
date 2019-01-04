#include "text.h"

Text::Text(std::string content):content(content){}

std::string Text::toHTML() const { return content; }

std::string Text::getContent() const
{
    return content;
}

void Text::setContent(const std::string &value)
{
    content = value;
}
