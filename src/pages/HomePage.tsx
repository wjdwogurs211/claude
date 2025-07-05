import HeroSection from '../components/sections/HeroSection';
import ServicesSection from '../components/sections/ServicesSection';
import ProcessSection from '../components/sections/ProcessSection';
import PricingSection from '../components/sections/PricingSection';
import TestimonialsSection from '../components/sections/TestimonialsSection';
import CTASection from '../components/sections/CTASection';

export default function HomePage() {
  return (
    <>
      <HeroSection />
      <ServicesSection />
      <ProcessSection />
      <PricingSection />
      <TestimonialsSection />
      <CTASection />
    </>
  );
}