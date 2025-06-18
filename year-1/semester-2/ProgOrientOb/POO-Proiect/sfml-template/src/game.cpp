#include "game.h"

namespace Game_Engine
{



//Private Functions
void Game::_InitWindow()
{
    this->window=new sf::RenderWindow(sf::VideoMode(800,600),"Game 3",
    sf::Style::Close | sf::Style::Titlebar);

}



//Constructors and destructors
Game::Game()
{
    this->_InitWindow();

}

Game::~Game()
{
    delete this->window;

} 


 
//Functions
void Game::Run()
{
    while(this->window->isOpen())
    {
        this->Update();
        this->Render();
    }

}

void Game::Update()
{

}

void Game::Render()
{
    this->window->clear();

    //Draw all the stuf



    this->window->display();

}



}//namespace Game_Engine