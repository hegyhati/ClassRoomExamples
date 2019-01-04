#include "text.h"

Text::Text(std::string content):content(content){}

std::string Text::toHTML() { return content; }
