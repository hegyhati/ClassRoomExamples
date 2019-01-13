#include "Run.hpp"

Date Run::getDate() const
{
  return date;
}

std::string Run::getName() const
{
  return name;
}

std::string Run::getType() const
{
  return type;
}

Run::~Run()
{

}
