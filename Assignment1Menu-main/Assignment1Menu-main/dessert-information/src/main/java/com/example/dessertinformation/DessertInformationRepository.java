package com.example.dessertinformation;

import org.springframework.data.jpa.repository.JpaRepository;

public interface DessertInformationRepository extends JpaRepository<DessertInformation, Long> {
	DessertInformation findById(int id);

}
