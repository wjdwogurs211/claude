import { motion } from 'framer-motion';
import { Star, Quote } from 'lucide-react';

export default function TestimonialsSection() {
  const testimonials = [
    {
      name: '김민지',
      location: '서울 강남구',
      rating: 5,
      text: '정말 꼼꼼하고 깨끗하게 청소해주셨어요. 특히 주방과 화장실이 새것처럼 반짝반짝해졌습니다. 다음에도 꼭 이용하고 싶어요!',
      service: '홈클리닝',
      date: '2024년 1월'
    },
    {
      name: '이준호',
      location: '서울 서초구',
      rating: 5,
      text: '이사 청소를 맡겼는데, 정말 만족스러웠습니다. 구석구석 깨끗하게 청소해주셔서 새 집에 입주하는 기분이었어요.',
      service: '이사청소',
      date: '2024년 1월'
    },
    {
      name: '박서연',
      location: '서울 송파구',
      rating: 5,
      text: '매달 정기 청소를 이용하고 있는데, 항상 친절하고 꼼꼼하게 해주셔서 너무 만족합니다. 시간도 정확하게 지켜주세요.',
      service: '정기청소',
      date: '2023년 12월'
    },
    {
      name: '최현우',
      location: '서울 마포구',
      rating: 5,
      text: '사무실 청소를 맡겼는데, 직원들이 모두 만족했습니다. 업무 시간 외에 깨끗하게 청소해주셔서 좋았어요.',
      service: '오피스클리닝',
      date: '2023년 12월'
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
            고객 후기
          </h2>
          <p className="text-xl text-gray-600 max-w-2xl mx-auto">
            클리닝랩을 이용하신 고객님들의 생생한 후기입니다
          </p>
        </motion.div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-4xl mx-auto">
          {testimonials.map((testimonial, index) => (
            <motion.div
              key={index}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6, delay: index * 0.1 }}
              className="card hover:shadow-lg transition-shadow duration-300"
            >
              <div className="p-6">
                {/* Quote Icon */}
                <Quote className="w-8 h-8 text-primary-200 mb-4" />
                
                {/* Rating */}
                <div className="flex mb-4">
                  {[...Array(testimonial.rating)].map((_, i) => (
                    <Star key={i} className="w-5 h-5 text-yellow-400 fill-current" />
                  ))}
                </div>

                {/* Text */}
                <p className="text-gray-700 mb-6 leading-relaxed">
                  "{testimonial.text}"
                </p>

                {/* Author Info */}
                <div className="border-t pt-4">
                  <div className="flex items-center justify-between">
                    <div>
                      <p className="font-semibold text-gray-900">{testimonial.name}</p>
                      <p className="text-sm text-gray-600">{testimonial.location}</p>
                    </div>
                    <div className="text-right">
                      <p className="text-sm font-medium text-primary-500">{testimonial.service}</p>
                      <p className="text-xs text-gray-500">{testimonial.date}</p>
                    </div>
                  </div>
                </div>
              </div>
            </motion.div>
          ))}
        </div>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6, delay: 0.4 }}
          className="text-center mt-12"
        >
          <div className="inline-flex items-center justify-center p-4 bg-primary-50 rounded-lg mb-4">
            <div className="text-center">
              <p className="text-3xl font-bold text-primary-500">4.9/5</p>
              <p className="text-sm text-gray-600">평균 평점</p>
            </div>
            <div className="mx-8 h-12 w-px bg-primary-200"></div>
            <div className="text-center">
              <p className="text-3xl font-bold text-primary-500">10,000+</p>
              <p className="text-sm text-gray-600">만족한 고객</p>
            </div>
          </div>
        </motion.div>
      </div>
    </section>
  );
}