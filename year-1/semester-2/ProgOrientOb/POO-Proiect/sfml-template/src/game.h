#ifndef GAME_H
#define GAME_H

#include <SFML/Graphics.hpp>
#include <SFML/Window.hpp>
#include <SFML/System.hpp>

#include <iostream>
#include <vector>
#include <ctime>
#include <sstream>

namespace Game_Engine
{


class Game
{
    private:
        sf::RenderWindow* window;

        //Private Functions
        void _InitWindow();

    public:
        //Constructors and destructors
        Game();
        virtual ~Game();

        //Functions
        void Run(); 

        void Update();
        void Render();

};




}// namespace Game_Engine

#endif // GAME_H