# Kubernetes Network Policy Examples

## 1. Deny All Ingress Traffic
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: deny-all-ingress
spec:
  podSelector: {}  # Applies to all pods in the namespace
  policyTypes:
  - Ingress
  ingress: []  # No ingress rules means no incoming traffic is allowed
```

## 2. Allow Traffic Only from Specific Namespace
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-from-specific-namespace
spec:
  podSelector:
    matchLabels:
      app: backend  # Target specific pods
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          purpose: production  # Only allow traffic from pods in namespace with this label
```

## 3. Allow Traffic from Specific Pods
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-frontend-to-backend
spec:
  podSelector:
    matchLabels:
      app: backend  # Target backend pods
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: frontend  # Only allow traffic from frontend pods
    ports:
    - protocol: TCP
      port: 80  # Only allow traffic on specific port
```

## 4. Complex Network Policy with Multiple Rules
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: multi-rule-network-policy
spec:
  podSelector:
    matchLabels:
      tier: backend
  policyTypes:
  - Ingress
  - Egress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: frontend
    - namespaceSelector:
        matchLabels:
          purpose: monitoring
    ports:
    - protocol: TCP
      port: 8080
  egress:
  - to:
    - ipBlock:
        cidr: 10.0.0.0/24  # Allow egress to specific IP range
    ports:
    - protocol: TCP
      port: 5432  # e.g., database port
```

## Network Policy Best Practices
- Use labels to select pods and control traffic
- Start with a deny-all policy
- Gradually add specific allow rules
- Separate ingress and egress rules
- Consider namespace-level and pod-level selectors
- Limit ports and protocols

## Key Concepts
- `podSelector`: Targets specific pods
- `namespaceSelector`: Controls traffic between namespaces
- `ingress`: Incoming traffic rules
- `egress`: Outgoing traffic rules
- `ipBlock`: Control traffic to specific IP ranges
