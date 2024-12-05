```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: secure-app-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: secure-app
  template:
    metadata:
      labels:
        app: secure-app
    spec:
      securityContext:
        # Apply cluster-level security settings
        runAsNonRoot: true
        fsGroup: 2000
      containers:
      - name: secure-container
        image: myapp:latest
        securityContext:
          # Container-specific security settings
          runAsUser: 1000
          runAsGroup: 3000
          allowPrivilegeEscalation: false
          readOnlyRootFilesystem: true
          capabilities:
            drop:
              - ALL
            add:
              - NET_BIND_SERVICE
        resources:
          limits:
            cpu: "500m"
            memory: "512Mi"
          requests:
            cpu: "250m"
            memory: "256Mi"
```

## Security Context Breakdown

### Cluster-Level Security Context
- `runAsNonRoot: true`: Prevents running containers as root
- `fsGroup: 2000`: Sets the group ID for volume access

### Container-Level Security Context
- `runAsUser: 1000`: Runs the container as a specific non-root user
- `runAsGroup: 3000`: Sets the group ID for the container
- `allowPrivilegeEscalation: false`: Prevents the container from gaining additional privileges
- `readOnlyRootFilesystem: true`: Makes the root filesystem read-only
- `capabilities`: 
  - `drop: [ALL]`: Removes all default Linux capabilities
  - `add: [NET_BIND_SERVICE]`: Adds only the necessary capability to bind to network ports

### Resource Constraints
- Limits CPU and memory usage to prevent resource exhaustion
