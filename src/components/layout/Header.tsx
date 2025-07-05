import { useState } from 'react';
import { Link } from 'react-router-dom';
import { Menu, X, Phone, Clock } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';

export default function Header() {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const menuItems = [
    { name: '회사소개', path: '/about' },
    { name: '홈클리닝', path: '/home_clean' },
    { name: '오피스클리닝', path: '/office_clean' },
    { name: '이사청소', path: '/move_clean' },
    { name: '입주청소', path: '/movein_clean' },
    { name: '예약문의', path: '/reservation' },
  ];

  return (
    <header className="sticky top-0 z-50 bg-white shadow-sm">
      {/* Top Bar */}
      <div className="bg-gray-50 border-b border-gray-200">
        <div className="container mx-auto px-4">
          <div className="flex items-center justify-between h-10 text-sm">
            <div className="flex items-center space-x-6">
              <div className="flex items-center text-gray-600">
                <Clock className="w-4 h-4 mr-1" />
                <span>평일 09:00 - 18:00</span>
              </div>
              <div className="flex items-center text-gray-600">
                <Phone className="w-4 h-4 mr-1" />
                <span className="font-medium">1588-4954</span>
              </div>
            </div>
            <div className="hidden md:flex items-center space-x-4">
              <Link to="/login" className="text-gray-600 hover:text-primary-500">
                로그인
              </Link>
              <span className="text-gray-300">|</span>
              <Link to="/signup" className="text-gray-600 hover:text-primary-500">
                회원가입
              </Link>
            </div>
          </div>
        </div>
      </div>

      {/* Main Navigation */}
      <nav className="bg-white">
        <div className="container mx-auto px-4">
          <div className="flex items-center justify-between h-16">
            {/* Logo */}
            <Link to="/" className="flex items-center">
              <div className="text-2xl font-bold text-primary-500">
                클리닝랩
              </div>
            </Link>

            {/* Desktop Menu */}
            <div className="hidden lg:flex items-center space-x-8">
              {menuItems.map((item) => (
                <Link
                  key={item.path}
                  to={item.path}
                  className="text-gray-700 hover:text-primary-500 font-medium transition-colors"
                >
                  {item.name}
                </Link>
              ))}
              <Link to="/reservation" className="btn-primary">
                예약하기
              </Link>
            </div>

            {/* Mobile Menu Button */}
            <button
              className="lg:hidden"
              onClick={() => setIsMenuOpen(!isMenuOpen)}
            >
              {isMenuOpen ? (
                <X className="w-6 h-6" />
              ) : (
                <Menu className="w-6 h-6" />
              )}
            </button>
          </div>
        </div>

        {/* Mobile Menu */}
        <AnimatePresence>
          {isMenuOpen && (
            <motion.div
              initial={{ opacity: 0, height: 0 }}
              animate={{ opacity: 1, height: 'auto' }}
              exit={{ opacity: 0, height: 0 }}
              className="lg:hidden bg-white border-t"
            >
              <div className="container mx-auto px-4 py-4">
                {menuItems.map((item) => (
                  <Link
                    key={item.path}
                    to={item.path}
                    className="block py-3 text-gray-700 hover:text-primary-500 font-medium"
                    onClick={() => setIsMenuOpen(false)}
                  >
                    {item.name}
                  </Link>
                ))}
                <Link
                  to="/reservation"
                  className="btn-primary w-full mt-4 text-center"
                  onClick={() => setIsMenuOpen(false)}
                >
                  예약하기
                </Link>
              </div>
            </motion.div>
          )}
        </AnimatePresence>
      </nav>
    </header>
  );
}