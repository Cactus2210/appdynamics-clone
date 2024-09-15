# Logic for comparing with the baseline of API performance
def compare_with_baseline(current_status, baseline_data):
    comparison_results = {}
    for api_url, current_data in current_status.items():
        baseline_latency = baseline_data.get(api_url, {}).get('latency', None)
        baseline_status_code = baseline_data.get(api_url, {}).get('status_code', None)
        
        if baseline_latency and baseline_status_code:
            comparison_results[api_url] = {
                'latency_change': current_data['latency'] - baseline_latency,
                'status_code_change': current_data['status_code'] != baseline_status_code
            }
        else:
            comparison_results[api_url] = {'error': 'No baseline data available'}
    
    return comparison_results
