package ru.apolyakov.airflow_workflow_service.config;

import com.sun.jersey.api.client.Client;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class AirflowHttpClientProvider {
    @Bean
    public Client createClient() {
        return Client.create();
    }
}

