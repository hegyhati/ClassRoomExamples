#include <iostream>
#include <random>

struct TemperatureElement
{
    double temp;
    double humidity;
    TemperatureElement* next;
};

struct TemperatureChain
{
    unsigned int cnt;
    TemperatureElement* first;
    TemperatureElement* last;
};

void reset(TemperatureChain*& chain)
{
    if (chain!=NULL)
    {
        TemperatureElement* elem = chain->first;
        while (elem != NULL)
        {
            TemperatureElement* tmp = elem;
            elem = elem->next;
            delete tmp;
        }
        delete chain;
        chain = NULL;
    }
}

void appendLast(TemperatureChain*& chain, const double temp, const double humidity)
{
    TemperatureElement* elem = new TemperatureElement();
    elem->next = NULL;
    if (chain==NULL)
    {
        chain = new TemperatureChain();
        chain->first = elem;
        chain->last = elem;
        chain->cnt = 1;
    }
    else
    {
        chain->last->next = elem;
        chain->last = elem;
        chain->cnt++;   
    }
    elem->temp = temp;
    elem->humidity = humidity;
}

bool temperatureComfortable(const TemperatureElement& temp)
{
    if (temp.temp < 15)
    {
        return false;
    }
    else if (temp.temp > 28)
    {
        return false;
    }   
    return true;
}

void addTemperatureElement(TemperatureChain*& chain)
{
    static std::random_device rd;
    static std::mt19937 gen(rd());
    static std::uniform_real_distribution<double> dis_temp(14.7, 28.3);
    static std::uniform_real_distribution<double> dis_humidity(0.0, 1.0);
    appendLast(chain, dis_temp(gen), dis_humidity(gen));
}

void print(TemperatureChain*& chain)
{
    TemperatureElement* elem = chain->first;
    while (elem->next != NULL)
    {
        std::cout << "Temperature: " << elem->temp << "\t" << elem->humidity << '\n';
        elem = elem->next;
    }
}

bool checkTemperature(TemperatureChain*& chain)
{
    TemperatureElement* elem = chain->first;
    while (elem->next != NULL)
    {
        if (!temperatureComfortable(*elem))
        {
            std::cerr << "Uncomfortable temperature reached" << '\n';
            return false;
        }
        elem = elem->next;
    }
    return true;
}

double avgTemperature(TemperatureChain*& chain)
{
    TemperatureElement* elem = chain->first;
    double temp = 0.0;
    while (elem->next != NULL)
    {
        if (!temperatureComfortable(*elem))
        {
            temp += elem->temp;
        }
        elem = elem->next;
    }
    return temp/((double)chain->cnt);
}

double maxTemperature(TemperatureChain*& chain)
{
    TemperatureElement* elem = chain->first;
    double max = 0.0;
    while (elem->next != NULL)
    {
        if (!temperatureComfortable(*elem))
        {
            if (elem->temp > max)
            {
                max = elem->temp;
            }
        }
        elem = elem->next;
    }
    return max;
}

constexpr int CHAIN_LENGTH = 10000;

int main(int argc, char** argv)
{
    TemperatureChain* chain = NULL;
    // Construct temperature chain
    for (int i = 0; i < CHAIN_LENGTH - 1; i++)
    {
        addTemperatureElement(chain);
    }
    print(chain);
    if (checkTemperature(chain))
    {
        std::cout << "Temperature OK\n";
    }
    else
    {
        std::cout << "Temperature is uncomfortable\n";
    }
    std::cout << "Average temperature: " << avgTemperature(chain) << '\n';
    std::cout << "Max temperature: " << maxTemperature(chain) << '\n';
    // Delete chain
    reset(chain);
    return 0;
}