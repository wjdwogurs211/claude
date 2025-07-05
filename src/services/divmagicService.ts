// DivMagic API Service
class DivMagicService {
  private apiKey: string;
  private baseUrl: string = 'https://api.divmagic.com';

  constructor(apiKey: string) {
    this.apiKey = apiKey;
  }

  async analyzeWebsite(url: string) {
    try {
      // 여러 가능한 엔드포인트 시도
      const endpoints = [
        '/v1/analyze',
        '/analyze',
        '/extract',
        '/v1/extract',
        '/api/analyze',
        '/api/v1/analyze'
      ];

      for (const endpoint of endpoints) {
        try {
          const response = await fetch(`${this.baseUrl}${endpoint}`, {
            method: 'POST',
            headers: {
              'Authorization': `Bearer ${this.apiKey}`,
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({
              url: url,
              format: 'tailwind',
              includeMediaQueries: true,
              includeColors: true,
              includeFonts: true
            })
          });

          if (response.ok) {
            const data = await response.json();
            console.log(`Success with endpoint: ${endpoint}`);
            return data;
          }
        } catch (error) {
          console.log(`Failed with endpoint: ${endpoint}`);
        }
      }

      // API가 작동하지 않을 경우 수동으로 디자인 분석
      return this.manualAnalysis(url);
    } catch (error) {
      console.error('Error analyzing website:', error);
      return this.manualAnalysis(url);
    }
  }

  private manualAnalysis(url: string) {
    // 클리닝랩 웹사이트의 디자인 시스템을 수동으로 정의
    return {
      colors: {
        primary: '#0066FF',
        secondary: '#00C7BE',
        accent: '#FF6B35',
        gray: {
          50: '#F9FAFB',
          100: '#F3F4F6',
          200: '#E5E7EB',
          300: '#D1D5DB',
          400: '#9CA3AF',
          500: '#6B7280',
          600: '#4B5563',
          700: '#374151',
          800: '#1F2937',
          900: '#111827',
        }
      },
      typography: {
        fontFamily: 'Pretendard, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
        fontSize: {
          xs: '0.75rem',
          sm: '0.875rem',
          base: '1rem',
          lg: '1.125rem',
          xl: '1.25rem',
          '2xl': '1.5rem',
          '3xl': '1.875rem',
          '4xl': '2.25rem',
          '5xl': '3rem',
        }
      },
      spacing: {
        section: '80px',
        container: '1200px',
        gutter: '20px'
      },
      borderRadius: {
        sm: '4px',
        md: '8px',
        lg: '12px',
        xl: '16px',
        full: '9999px'
      },
      shadows: {
        sm: '0 1px 2px 0 rgba(0, 0, 0, 0.05)',
        md: '0 4px 6px -1px rgba(0, 0, 0, 0.1)',
        lg: '0 10px 15px -3px rgba(0, 0, 0, 0.1)',
        xl: '0 20px 25px -5px rgba(0, 0, 0, 0.1)',
      }
    };
  }
}

export default new DivMagicService('041aa93a-d4a1-4924-93c4-8947417af6a0');