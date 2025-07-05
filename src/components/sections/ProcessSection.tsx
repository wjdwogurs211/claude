import { motion } from 'framer-motion';
import { Phone, Calendar, Users, CheckCircle2 } from 'lucide-react';

export default function ProcessSection() {
  const steps = [
    {
      icon: <Phone className="w-8 h-8" />,
      title: '상담 신청',
      description: '전화 또는 온라인으로 간편하게 상담을 신청하세요.',
      number: '01'
    },
    {
      icon: <Calendar className="w-8 h-8" />,
      title: '일정 조율',
      description: '고객님께 가장 편리한 시간으로 방문 일정을 조율합니다.',
      number: '02'
    },
    {
      icon: <Users className="w-8 h-8" />,
      title: '전문가 방문',
      description: '교육받은 전문 청소팀이 약속된 시간에 방문합니다.',
      number: '03'
    },
    {
      icon: <CheckCircle2 className="w-8 h-8" />,
      title: '서비스 완료',
      description: '꼼꼼한 청소 후 고객님의 확인을 받고 서비스를 완료합니다.',
      number: '04'
    }
  ];

  return (
    <section className="section-padding bg-white">
      <div className="container mx-auto px-4">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
          className="text-center mb-12"
        >
          <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
            서비스 진행 과정
          </h2>
          <p className="text-xl text-gray-600 max-w-2xl mx-auto">
            간단한 4단계로 클리닝랩의 전문 청소 서비스를 경험하세요
          </p>
        </motion.div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          {steps.map((step, index) => (
            <motion.div
              key={index}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6, delay: index * 0.1 }}
              className="relative"
            >
              {/* Connection Line */}
              {index < steps.length - 1 && (
                <div className="hidden lg:block absolute top-16 left-full w-full h-0.5 bg-gray-300 -z-10">
                  <div className="absolute right-0 top-1/2 transform -translate-y-1/2">
                    <div className="w-0 h-0 border-t-4 border-t-transparent border-b-4 border-b-transparent border-l-4 border-l-gray-300"></div>
                  </div>
                </div>
              )}

              <div className="text-center">
                {/* Number */}
                <div className="text-5xl font-bold text-primary-100 mb-4">
                  {step.number}
                </div>

                {/* Icon */}
                <div className="inline-flex items-center justify-center w-16 h-16 bg-primary-500 text-white rounded-full mb-4">
                  {step.icon}
                </div>

                {/* Content */}
                <h3 className="text-xl font-semibold text-gray-900 mb-2">
                  {step.title}
                </h3>
                <p className="text-gray-600">
                  {step.description}
                </p>
              </div>
            </motion.div>
          ))}
        </div>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6, delay: 0.4 }}
          className="mt-12 bg-primary-50 rounded-2xl p-8 text-center"
        >
          <h3 className="text-2xl font-semibold text-gray-900 mb-4">
            지금 바로 시작하세요!
          </h3>
          <p className="text-gray-600 mb-6">
            전화 한 통으로 깨끗한 공간을 만들어드립니다
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <a href="tel:1588-4954" className="btn-primary">
              <Phone className="w-5 h-5 mr-2" />
              1588-4954
            </a>
            <Link to="/reservation" className="btn-secondary">
              온라인 예약
            </Link>
          </div>
        </motion.div>
      </div>
    </section>
  );
}

// Link import 추가
import { Link } from 'react-router-dom';