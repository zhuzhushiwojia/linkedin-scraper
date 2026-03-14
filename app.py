#!/usr/bin/env python3
"""
LinkedIn Scraper API - Railway Deployment
Flask web service for LinkedIn data enrichment
"""

from flask import Flask, jsonify, request
from linkedin_scraper import LinkedInScraper
import os

app = Flask(__name__)
scraper = LinkedInScraper(use_proxy=False)

@app.route('/api/linkedin/person', methods=['GET'])
def get_person():
    """Get LinkedIn person profile"""
    url = request.args.get('url', '')
    if not url:
        return jsonify({'error': 'Missing url parameter'}), 400
    
    profile = scraper.scrape_profile(url)
    if profile:
        return jsonify(profile)
    return jsonify({'error': 'Failed to scrape profile'}), 500

@app.route('/api/linkedin/company', methods=['GET'])
def get_company():
    """Get LinkedIn company profile"""
    url = request.args.get('url', '')
    if not url:
        return jsonify({'error': 'Missing url parameter'}), 400
    
    company = scraper.scrape_company(url)
    if company:
        return jsonify(company)
    return jsonify({'error': 'Failed to scrape company'}), 500

@app.route('/api/linkedin/search/people', methods=['GET'])
def search_people():
    """Search LinkedIn people"""
    keywords = request.args.get('keywords', 'software engineer')
    limit = int(request.args.get('limit', 10))
    
    results = scraper.search_profiles(keywords, limit)
    return jsonify({'results': results, 'count': len(results)})

@app.route('/api/linkedin/search/companies', methods=['GET'])
def search_companies():
    """Search LinkedIn companies"""
    keywords = request.args.get('keywords', 'technology')
    limit = int(request.args.get('limit', 5))
    
    results = scraper.search_companies(keywords, limit)
    return jsonify({'results': results, 'count': len(results)})

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'service': 'linkedin-scraper'})

@app.route('/', methods=['GET'])
def index():
    """API documentation"""
    return jsonify({
        'service': 'LinkedIn Scraper API',
        'version': '1.0.0',
        'endpoints': [
            'GET /api/linkedin/person?url=<linkedin_profile_url>',
            'GET /api/linkedin/company?url=<linkedin_company_url>',
            'GET /api/linkedin/search/people?keywords=<keywords>&limit=<limit>',
            'GET /api/linkedin/search/companies?keywords=<keywords>&limit=<limit>',
            'GET /health'
        ],
        'demo': 'Visit /api/linkedin/search/people?keywords=software+engineer&limit=10'
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
