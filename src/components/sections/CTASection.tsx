import { motion } from 'framer-motion';
import { Phone, MessageCircle, ArrowRight } from 'lucide-react';
import { Link } from 'react-router-dom';

export default function CTASection() {
  return (
    <section className="bg-gradient-to-br from-primary-500 to-primary-600 text-white">
      <div className="container mx-auto px-4 py-16 md:py-20">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
          className="text-center max-w-3xl mx-auto"
        >
          <h2 className="text-3xl md:text-4xl font-bold mb-4">
            지금 바로 깨끗한 변화를 시작하세요
          </h2>
          <p className="text-xl text-primary-100 mb-8">
            전문가의 손길로 만드는 깨끗하고 건강한 공간,<br />
            클리닝랩이 함께합니다
          </p>

          <div className="flex flex-col sm:flex-row gap-4 justify-center mb-8">
            <a
              href="tel:1588-4954"
              className="inline-flex items-center justify-center px-8 py-4 bg-white text-primary-500 font-medium rounded-lg hover:bg-gray-100 transition-colors duration-200 shadow-lg"
            >
              <Phone className="w-5 h-5 mr-2" />
              1588-4954 전화상담
            </a>
            <Link
              to="/reservation"
              className="inline-flex items-center justify-center px-8 py-4 bg-primary-700 text-white font-medium rounded-lg hover:bg-primary-800 transition-colors duration-200 shadow-lg"
            >
              온라인 예약하기
              <ArrowRight className="w-5 h-5 ml-2" />
            </Link>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-12">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6, delay: 0.1 }}
              className="bg-white/10 backdrop-blur-sm rounded-lg p-6"
            >
              <h3 className="text-xl font-semibold mb-2">빠른 예약</h3>
              <p className="text-primary-100">
                24시간 온라인 예약 가능<br />
                당일 예약도 OK
              </p>
            </motion.div>

            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6, delay: 0.2 }}
              className="bg-white/10 backdrop-blur-sm rounded-lg p-6"
            >
              <h3 className="text-xl font-semibold mb-2">합리적 가격</h3>
              <p className="text-primary-100">
                투명한 요금 체계<br />
                숨겨진 비용 없음
              </p>
            </motion.div>

            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6, delay: 0.3 }}
              className="bg-white/10 backdrop-blur-sm rounded-lg p-6"
            >
              <h3 className="text-xl font-semibold mb-2">만족 보장</h3>
              <p className="text-primary-100">
                100% 만족 보장 서비스<br />
                불만족시 재청소
              </p>
            </motion.div>
          </div>

          {/* Floating Chat Button */}
          <motion.button
            initial={{ scale: 0 }}
            animate={{ scale: 1 }}
            transition={{ duration: 0.3, delay: 1 }}
            className="fixed bottom-6 right-6 z-40 bg-primary-500 text-white p-4 rounded-full shadow-lg hover:bg-primary-600 transition-colors"
            onClick={() => console.log('Open chat')}
          >
            <MessageCircle className="w-6 h-6" />
          </motion.button>
        </motion.div>
      </div>
    </section>
  );
}