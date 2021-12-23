package com.customer;

import lombok.Data;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection="customer")
@Data
public class Customer {
    @Id
    private Long id;
    private String name;

    // Getters and Setters
}
