import { motion } from 'framer-motion';
import { Home, Clock, Users, Shield, Sparkles, CheckCircle } from 'lucide-react';
import { Link } from 'react-router-dom';

export default function HomeCleanPage() {
  const features = [
    {
      icon: <Clock className="w-6 h-6" />,
      title: '시간제 서비스',
      description: '필요한 시간만큼 서비스를 이용하실 수 있습니다.'
    },
    {
      icon: <Users className="w-6 h-6" />,
      title: '전문 청소팀',
      description: '체계적인 교육을 받은 전문가가 방문합니다.'
    },
    {
      icon: <Shield className="w-6 h-6" />,
      title: '손해배상책임보험',
      description: '서비스 중 발생할 수 있는 사고에 대비했습니다.'
    },
    {
      icon: <Sparkles className="w-6 h-6" />,
      title: '친환경 청소',
      description: '인체에 무해한 친환경 세제를 사용합니다.'
    }
  ];

  const serviceDetails = [
    '거실 및 방 청소',
    '주방 청소 (싱크대, 가스레인지, 후드)',
    '욕실 청소 (변기, 세면대, 욕조)',
    '바닥 청소 (먼지제거, 물걸레)',
    '창문 및 창틀 청소',
    '가전제품 외부 청소',
    '쓰레기 정리 및 분리수거',
    '침구류 정리'
  ];

  const pricingOptions = [
    {
      duration: '2시간',
      price: '50,000원',
      size: '~20평',
      description: '원룸, 소형 아파트'
    },
    {
      duration: '3시간',
      price: '70,000원',
      size: '20~30평',
      description: '일반 아파트',
      popular: true
    },
    {
      duration: '4시간',
      price: '90,000원',
      size: '30~40평',
      description: '대형 아파트'
    },
    {
      duration: '5시간+',
      price: '별도 문의',
      size: '40평+',
      description: '복층, 단독주택'
    }
  ];

  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="bg-gradient-to-br from-blue-50 to-white py-20">
        <div className="container mx-auto px-4">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
            className="max-w-4xl mx-auto text-center"
          >
            <div className="inline-flex items-center justify-center w-20 h-20 bg-blue-100 rounded-full mb-6">
              <Home className="w-10 h-10 text-blue-500" />
            </div>
            <h1 className="text-4xl md:text-5xl font-bold text-gray-900 mb-6">
              홈클리닝 서비스
            </h1>
            <p className="text-xl text-gray-600 mb-8 max-w-2xl mx-auto">
              바쁜 일상 속에서도 깨끗한 집을 유지하고 싶으신가요?<br />
              클리닝랩의 전문가가 당신의 소중한 공간을 관리해드립니다.
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Link to="/reservation" className="btn-primary">
                지금 예약하기
              </Link>
              <a href="tel:1588-4954" className="btn-secondary">
                전화 상담하기
              </a>
            </div>
          </motion.div>
        </div>
      </section>

      {/* Features Section */}
      <section className="section-padding bg-gray-50">
        <div className="container mx-auto px-4">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6 }}
            className="text-center mb-12"
          >
            <h2 className="text-3xl font-bold text-gray-900 mb-4">
              왜 클리닝랩 홈클리닝인가요?
            </h2>
          </motion.div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 max-w-5xl mx-auto">
            {features.map((feature, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.6, delay: index * 0.1 }}
                className="card p-6 text-center"
              >
                <div className="inline-flex items-center justify-center w-14 h-14 bg-blue-100 text-blue-500 rounded-full mb-4">
                  {feature.icon}
                </div>
                <h3 className="text-lg font-semibold text-gray-900 mb-2">
                  {feature.title}
                </h3>
                <p className="text-gray-600">
                  {feature.description}
                </p>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Service Details Section */}
      <section className="section-padding bg-white">
        <div className="container mx-auto px-4">
          <div className="max-w-5xl mx-auto">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6 }}
              className="text-center mb-12"
            >
              <h2 className="text-3xl font-bold text-gray-900 mb-4">
                서비스 상세 내용
              </h2>
              <p className="text-xl text-gray-600">
                클리닝랩 홈클리닝 서비스에 포함된 항목입니다
              </p>
            </motion.div>

            <div className="grid md:grid-cols-2 gap-12 items-center">
              <motion.div
                initial={{ opacity: 0, x: -50 }}
                whileInView={{ opacity: 1, x: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.6 }}
              >
                <div className="bg-gradient-to-br from-blue-50 to-blue-100 rounded-2xl p-8">
                  <h3 className="text-2xl font-bold text-gray-900 mb-6">
                    기본 청소 항목
                  </h3>
                  <ul className="space-y-3">
                    {serviceDetails.map((item, index) => (
                      <li key={index} className="flex items-start">
                        <CheckCircle className="w-5 h-5 text-blue-500 mr-3 flex-shrink-0 mt-0.5" />
                        <span className="text-gray-700">{item}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              </motion.div>

              <motion.div
                initial={{ opacity: 0, x: 50 }}
                whileInView={{ opacity: 1, x: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.6 }}
                className="space-y-6"
              >
                <div className="card p-6">
                  <h4 className="text-xl font-semibold text-gray-900 mb-3">
                    추가 가능 서비스
                  </h4>
                  <ul className="space-y-2 text-gray-600">
                    <li>• 냉장고 내부 청소</li>
                    <li>• 오븐/전자레인지 내부 청소</li>
                    <li>• 베란다 청소</li>
                    <li>• 정리수납 서비스</li>
                  </ul>
                </div>

                <div className="card p-6 bg-blue-50">
                  <h4 className="text-xl font-semibold text-gray-900 mb-3">
                    준비사항
                  </h4>
                  <p className="text-gray-700">
                    귀중품은 미리 보관해주시고, 청소 도구나 세제는 
                    저희가 준비해갑니다. 특별히 사용을 원하시는 
                    세제가 있으시면 말씀해주세요.
                  </p>
                </div>
              </motion.div>
            </div>
          </div>
        </div>
      </section>

      {/* Pricing Section */}
      <section className="section-padding bg-gray-50">
        <div className="container mx-auto px-4">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6 }}
            className="text-center mb-12"
          >
            <h2 className="text-3xl font-bold text-gray-900 mb-4">
              요금 안내
            </h2>
            <p className="text-xl text-gray-600">
              공간 크기와 필요 시간에 따라 선택하세요
            </p>
          </motion.div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 max-w-6xl mx-auto">
            {pricingOptions.map((option, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.6, delay: index * 0.1 }}
                className={`card p-6 text-center ${option.popular ? 'ring-2 ring-primary-500' : ''}`}
              >
                {option.popular && (
                  <span className="inline-block bg-primary-500 text-white text-sm px-3 py-1 rounded-full mb-4">
                    인기
                  </span>
                )}
                <h3 className="text-2xl font-bold text-gray-900 mb-2">
                  {option.duration}
                </h3>
                <p className="text-3xl font-bold text-primary-500 mb-2">
                  {option.price}
                </p>
                <p className="text-gray-600 mb-2">{option.size}</p>
                <p className="text-sm text-gray-500">{option.description}</p>
              </motion.div>
            ))}
          </div>

          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6, delay: 0.4 }}
            className="mt-8 text-center"
          >
            <p className="text-gray-600 mb-6">
              * 정기 이용시 10~20% 할인 혜택이 있습니다<br />
              * 첫 이용 고객님께는 30% 할인을 제공합니다
            </p>
            <Link to="/reservation" className="btn-primary">
              예약하고 할인받기
            </Link>
          </motion.div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="bg-primary-500 text-white py-16">
        <div className="container mx-auto px-4 text-center">
          <h2 className="text-3xl font-bold mb-4">
            지금 바로 깨끗한 우리집을 만나보세요
          </h2>
          <p className="text-xl text-primary-100 mb-8">
            전문가의 손길로 완성되는 완벽한 청소
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <a
              href="tel:1588-4954"
              className="inline-flex items-center justify-center px-8 py-4 bg-white text-primary-500 font-medium rounded-lg hover:bg-gray-100 transition-colors"
            >
              <Phone className="w-5 h-5 mr-2" />
              1588-4954
            </a>
            <Link
              to="/reservation"
              className="inline-flex items-center justify-center px-8 py-4 bg-primary-600 text-white font-medium rounded-lg hover:bg-primary-700 transition-colors"
            >
              온라인 예약하기
            </Link>
          </div>
        </div>
      </section>
    </div>
  );
}

// Phone import 추가
import { Phone } from 'lucide-react';