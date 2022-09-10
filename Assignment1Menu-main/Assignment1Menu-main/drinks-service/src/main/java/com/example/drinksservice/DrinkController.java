package com.example.drinksservice;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.env.Environment;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class DrinkController {

    @Autowired
    private DrinkRepository repository;
    @Autowired
    private Environment environment;

    @GetMapping("/drinks/id/{id}")
    public Drink retrieveDrinkValue(@PathVariable int id){

        Drink drink = repository.findById(id);

        if(drink==null)
            throw new RuntimeException("Unable to find data on the drink");

        String port = environment.getProperty("local.server.port");
        drink.setEnvironment(port);

        return drink;
    }
}
