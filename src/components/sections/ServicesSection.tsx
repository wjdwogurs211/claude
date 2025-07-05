import { motion } from 'framer-motion';
import { Home, Building, Truck, Sparkles, Calendar, Shield } from 'lucide-react';
import { Link } from 'react-router-dom';

export default function ServicesSection() {
  const services = [
    {
      icon: <Home className="w-8 h-8" />,
      title: '홈클리닝',
      description: '가정집 청소 전문 서비스로 깨끗하고 쾌적한 주거 환경을 만들어드립니다.',
      link: '/home_clean',
      color: 'bg-blue-50 text-blue-500'
    },
    {
      icon: <Building className="w-8 h-8" />,
      title: '오피스클리닝',
      description: '사무실과 상업 공간을 위한 전문적이고 체계적인 청소 서비스입니다.',
      link: '/office_clean',
      color: 'bg-green-50 text-green-500'
    },
    {
      icon: <Truck className="w-8 h-8" />,
      title: '이사청소',
      description: '이사 전후 완벽한 청소로 새로운 시작을 깨끗하게 준비해드립니다.',
      link: '/move_clean',
      color: 'bg-purple-50 text-purple-500'
    },
    {
      icon: <Sparkles className="w-8 h-8" />,
      title: '입주청소',
      description: '새 집 입주 전 구석구석 꼼꼼한 청소로 완벽한 입주를 도와드립니다.',
      link: '/movein_clean',
      color: 'bg-orange-50 text-orange-500'
    },
    {
      icon: <Calendar className="w-8 h-8" />,
      title: '정기청소',
      description: '주기적인 방문으로 항상 깨끗한 환경을 유지할 수 있도록 관리해드립니다.',
      link: '/regular_clean',
      color: 'bg-pink-50 text-pink-500'
    },
    {
      icon: <Shield className="w-8 h-8" />,
      title: '특수청소',
      description: '곰팡이 제거, 바닥 왁싱 등 특별한 청소가 필요한 경우를 위한 서비스입니다.',
      link: '/special_clean',
      color: 'bg-indigo-50 text-indigo-500'
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
            클리닝랩 서비스
          </h2>
          <p className="text-xl text-gray-600 max-w-2xl mx-auto">
            고객님의 니즈에 맞춘 다양한 청소 서비스를 제공합니다
          </p>
        </motion.div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {services.map((service, index) => (
            <motion.div
              key={index}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6, delay: index * 0.1 }}
            >
              <Link
                to={service.link}
                className="block h-full card hover:shadow-lg transition-all duration-300 group"
              >
                <div className="p-6">
                  <div className={`inline-flex p-3 rounded-lg ${service.color} mb-4 group-hover:scale-110 transition-transform`}>
                    {service.icon}
                  </div>
                  <h3 className="text-xl font-semibold text-gray-900 mb-2 group-hover:text-primary-500 transition-colors">
                    {service.title}
                  </h3>
                  <p className="text-gray-600">
                    {service.description}
                  </p>
                </div>
              </Link>
            </motion.div>
          ))}
        </div>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6, delay: 0.6 }}
          className="text-center mt-12"
        >
          <Link to="/services" className="btn-primary">
            모든 서비스 보기
            <ArrowRight className="w-5 h-5 ml-2" />
          </Link>
        </motion.div>
      </div>
    </section>
  );
}

// ArrowRight import 추가
import { ArrowRight } from 'lucide-react';