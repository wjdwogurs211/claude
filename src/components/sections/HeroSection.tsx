import { motion } from 'framer-motion';
import { ArrowRight, CheckCircle } from 'lucide-react';
import { Link } from 'react-router-dom';

export default function HeroSection() {
  const features = [
    '전문 교육을 받은 청소 전문가',
    '친환경 프리미엄 청소 용품',
    '100% 만족 보장 서비스',
    '합리적인 가격'
  ];

  return (
    <section className="relative bg-gradient-to-br from-primary-50 to-white overflow-hidden">
      <div className="container mx-auto px-4 py-20 lg:py-32">
        <div className="grid lg:grid-cols-2 gap-12 items-center">
          {/* Content */}
          <motion.div
            initial={{ opacity: 0, x: -50 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.6 }}
          >
            <h1 className="text-4xl md:text-5xl lg:text-6xl font-bold text-gray-900 mb-6">
              깨끗한 공간,<br />
              <span className="text-primary-500">행복한 일상</span>
            </h1>
            <p className="text-xl text-gray-600 mb-8">
              클리닝랩의 전문 청소 서비스로<br />
              더 나은 생활 환경을 만들어보세요.
            </p>

            {/* Features */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 mb-8">
              {features.map((feature, index) => (
                <motion.div
                  key={index}
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ duration: 0.6, delay: index * 0.1 }}
                  className="flex items-center text-gray-700"
                >
                  <CheckCircle className="w-5 h-5 text-primary-500 mr-2 flex-shrink-0" />
                  <span>{feature}</span>
                </motion.div>
              ))}
            </div>

            {/* CTA Buttons */}
            <div className="flex flex-col sm:flex-row gap-4">
              <Link to="/reservation" className="btn-primary">
                예약하기
                <ArrowRight className="w-5 h-5 ml-2" />
              </Link>
              <Link to="/about" className="btn-secondary">
                서비스 둘러보기
              </Link>
            </div>
          </motion.div>

          {/* Hero Image/Graphic */}
          <motion.div
            initial={{ opacity: 0, x: 50 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.6, delay: 0.2 }}
            className="relative"
          >
            <div className="relative z-10">
              <div className="bg-gradient-to-br from-primary-100 to-primary-50 rounded-3xl p-8 lg:p-12">
                <div className="bg-white rounded-2xl shadow-xl p-6">
                  <h3 className="text-2xl font-bold text-gray-900 mb-4">
                    지금 예약하고<br />특별 할인 받으세요!
                  </h3>
                  <div className="space-y-3">
                    <div className="flex items-center justify-between">
                      <span className="text-gray-600">첫 이용 고객</span>
                      <span className="text-2xl font-bold text-primary-500">30% 할인</span>
                    </div>
                    <div className="flex items-center justify-between">
                      <span className="text-gray-600">정기 서비스</span>
                      <span className="text-2xl font-bold text-primary-500">20% 할인</span>
                    </div>
                  </div>
                  <Link to="/reservation" className="btn-primary w-full mt-6 text-center">
                    지금 바로 예약
                  </Link>
                </div>
              </div>
            </div>
            
            {/* Decorative Elements */}
            <div className="absolute top-0 right-0 -mt-4 -mr-4 w-24 h-24 bg-primary-200 rounded-full opacity-50 blur-xl"></div>
            <div className="absolute bottom-0 left-0 -mb-4 -ml-4 w-32 h-32 bg-primary-300 rounded-full opacity-30 blur-xl"></div>
          </motion.div>
        </div>
      </div>

      {/* Background Pattern */}
      <div className="absolute inset-0 opacity-5">
        <div className="absolute inset-0" style={{
          backgroundImage: `url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%230066FF' fill-opacity='1'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E")`
        }}></div>
      </div>
    </section>
  );
}