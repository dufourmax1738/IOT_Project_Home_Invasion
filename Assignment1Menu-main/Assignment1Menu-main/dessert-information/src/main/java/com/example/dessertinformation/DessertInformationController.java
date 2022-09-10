package com.example.dessertinformation;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class DessertInformationController {
	
	@Autowired
	private DessertInformationRepository repository;
	
	
	@GetMapping("/dessert-information/id/{id}")
	public DessertInformation retrieveExchangeValue(@PathVariable int id) {
		
		
		DessertInformation dessert = repository.findById(id);
		
		return dessert;
		
	}
	
	
}
