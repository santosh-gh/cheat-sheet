# DevSecOps
    - Continiously Access: Identify and track vulnerabilities.
    - Security: Harden resources and services with Azure Security Benchmark.
    - Detect and resolve threats to resources, workloads and services.

# Phases
    - Analyze - Identify critical security challanges
    - Secure - Implement a defence strategy for that challenges
    - Secure - Implement a defence strategy for that challenges
    - Verify - Automate the security testing for that challenge

# Plan(Analyze - Identify critical security challanges)
    - Thread Modeling (It is a cyclic process)
        1. Identify the Assets
        2. Outline Architecture
        3. Break Down the Application
        4. Identify Treats
        5. Classify & Structure Threats
        6. Rate Severity of Threats	

        Tools:
    
# Code(Secure - Implement a defence strategy for that challenges)
    - Coding Best Practices (Security as Code)
        1. Input validation and output encoding
        2. Authentication and Authorization
        3. Session Management
        4. Encryption of sensitive data
        5. Secure system configuration
        6. Error handling, Auditing and Logging
        7. Data Protection and Transmission
        
        Tools: OWASP		
    
# Test(Verify - Automate the security testing for that challenge)
    - Security Testing
        1. SAST
            - White box Testing
            - Requires Source Code
            - Earlier detection
            - Doesn't find environment issues
            - Supports all software
            
        2. DAST
            - Black box testing
            - Requires Web Applications in staging or production
            - Later detection 
            - Find Environment issues
            - Predominantly Web App testing
        Tools: SonarQube, VERACODE		   
    
# Monitor(Defend - Detect attackes and protect explotes for that challenge)
    - Attack Detection & Prevention
        1. Runtime Application Self Protection (RASP)
            - Application instrumenation to add attack detection and prevention direcly to applications regardless of where or how they are deployed.
        2. Web Application Firewall (WAF)
            - Azure Application Gateway WAF
        3. Network Intrusion Detection and Prevention (IDS/IPS)