import { motion } from 'framer-motion';
import { Check, X } from 'lucide-react';
import { Link } from 'react-router-dom';

export default function PricingSection() {
  const plans = [
    {
      name: '베이직',
      price: '50,000',
      duration: '2시간',
      features: [
        { text: '기본 청소 서비스', included: true },
        { text: '친환경 청소 용품', included: true },
        { text: '2명 전문가 방문', included: true },
        { text: '주방 특수 청소', included: false },
        { text: '베란다 청소', included: false },
        { text: '정리 수납 서비스', included: false }
      ],
      recommended: false
    },
    {
      name: '스탠다드',
      price: '80,000',
      duration: '3시간',
      features: [
        { text: '기본 청소 서비스', included: true },
        { text: '친환경 청소 용품', included: true },
        { text: '2명 전문가 방문', included: true },
        { text: '주방 특수 청소', included: true },
        { text: '베란다 청소', included: true },
        { text: '정리 수납 서비스', included: false }
      ],
      recommended: true
    },
    {
      name: '프리미엄',
      price: '120,000',
      duration: '4시간',
      features: [
        { text: '기본 청소 서비스', included: true },
        { text: '친환경 청소 용품', included: true },
        { text: '3명 전문가 방문', included: true },
        { text: '주방 특수 청소', included: true },
        { text: '베란다 청소', included: true },
        { text: '정리 수납 서비스', included: true }
      ],
      recommended: false
    }
  ];

  return (
    <section className="section-padding bg-gray-50">
      <div className="container mx-auto px-4">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
          className="text-center mb-12"
        >
          <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
            서비스 요금안내
          </h2>
          <p className="text-xl text-gray-600 max-w-2xl mx-auto">
            고객님의 공간과 필요에 맞는 플랜을 선택하세요
          </p>
        </motion.div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-5xl mx-auto">
          {plans.map((plan, index) => (
            <motion.div
              key={index}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6, delay: index * 0.1 }}
              className={`relative card ${plan.recommended ? 'ring-2 ring-primary-500' : ''}`}
            >
              {plan.recommended && (
                <div className="absolute -top-4 left-1/2 transform -translate-x-1/2">
                  <span className="bg-primary-500 text-white px-4 py-1 rounded-full text-sm font-medium">
                    추천
                  </span>
                </div>
              )}

              <div className="p-6">
                <h3 className="text-2xl font-bold text-gray-900 mb-2">{plan.name}</h3>
                <div className="mb-6">
                  <span className="text-4xl font-bold text-primary-500">₩{plan.price}</span>
                  <span className="text-gray-600 ml-2">/ {plan.duration}</span>
                </div>

                <ul className="space-y-3 mb-8">
                  {plan.features.map((feature, featureIndex) => (
                    <li key={featureIndex} className="flex items-center">
                      {feature.included ? (
                        <Check className="w-5 h-5 text-green-500 mr-3 flex-shrink-0" />
                      ) : (
                        <X className="w-5 h-5 text-gray-300 mr-3 flex-shrink-0" />
                      )}
                      <span className={feature.included ? 'text-gray-700' : 'text-gray-400'}>
                        {feature.text}
                      </span>
                    </li>
                  ))}
                </ul>

                <Link
                  to="/reservation"
                  className={`block text-center ${
                    plan.recommended ? 'btn-primary' : 'btn-secondary'
                  }`}
                >
                  선택하기
                </Link>
              </div>
            </motion.div>
          ))}
        </div>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6, delay: 0.3 }}
          className="mt-12 text-center"
        >
          <p className="text-gray-600 mb-4">
            * 모든 가격은 VAT 포함이며, 평형별 추가 요금이 발생할 수 있습니다.
          </p>
          <Link to="/pricing" className="text-primary-500 hover:text-primary-600 font-medium">
            자세한 요금 정책 보기 →
          </Link>
        </motion.div>
      </div>
    </section>
  );
}