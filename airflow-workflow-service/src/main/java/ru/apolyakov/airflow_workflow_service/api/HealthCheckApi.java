package ru.apolyakov.airflow_workflow_service.api;

import javax.annotation.security.PermitAll;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.context.annotation.RequestScope;

@RestController
@RequestScope
public class HealthCheckApi {

    @PermitAll
    @GetMapping("/liveness_check")
    public ResponseEntity<String> livenessCheck() {
        return new ResponseEntity<>("Workflow service is alive", HttpStatus.OK);
    }

    @PermitAll
    @GetMapping("/readiness_check")
    public ResponseEntity<String> readinessCheck() {
        return new ResponseEntity<>("Workflow service is ready", HttpStatus.OK);
    }

}

